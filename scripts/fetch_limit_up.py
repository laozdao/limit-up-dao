"""
涨停股数据采集脚本
使用AkShare获取指定日期的涨停池、龙虎榜、板块数据，输出JSON供归因分析使用。

用法:
    python fetch_limit_up.py                    # 获取最近交易日
    python fetch_limit_up.py 20260521           # 获取指定日期
    python fetch_limit_up.py 20260521 --output  # 输出到文件

依赖:
    pip install akshare

输出: JSON格式的涨停股数据，包含涨停池、龙虎榜、板块信息
"""

import akshare as ak
import pandas as pd
import json
import sys
import argparse
import time
from datetime import datetime, date, timedelta
from pathlib import Path


def get_last_trading_day() -> str:
    """获取最近一个交易日(简化版，跳过周末)"""
    today = date.today()
    if today.weekday() == 5:
        today -= timedelta(days=1)
    elif today.weekday() == 6:
        today -= timedelta(days=2)
    # 如果当前时间在15:00前，取前一个交易日
    if datetime.now().hour < 15:
        today -= timedelta(days=1)
        if today.weekday() == 5:
            today -= timedelta(days=1)
        elif today.weekday() == 6:
            today -= timedelta(days=2)
    return today.strftime("%Y%m%d")


def fetch_limit_pool(trade_date: str) -> pd.DataFrame:
    """获取涨停池数据"""
    try:
        time.sleep(0.5)
        df = ak.stock_zt_pool_em(date=trade_date)
        if df is None or df.empty:
            return pd.DataFrame()
        
        # 标准化列名
        col_map = {}
        for col in df.columns:
            if "代码" in col:
                col_map[col] = "ts_code"
            elif "名称" in col:
                col_map[col] = "name"
            elif "涨跌幅" in col:
                col_map[col] = "pct_chg"
            elif "最新价" in col or "收盘价" in col:
                col_map[col] = "close"
            elif "成交额" in col:
                col_map[col] = "amount"
            elif "流通市值" in col:
                col_map[col] = "float_mv"
            elif "总市值" in col:
                col_map[col] = "total_mv"
            elif "换手率" in col:
                col_map[col] = "turnover"
            elif "连板数" in col:
                col_map[col] = "limit_count"
            elif "封板资金" in col:
                col_map[col] = "seal_amount"
            elif "首次封板时间" in col:
                col_map[col] = "first_limit_time"
            elif "最后封板时间" in col:
                col_map[col] = "last_limit_time"
            elif "炸板次数" in col:
                col_map[col] = "break_count"
            elif "所属行业" in col:
                col_map[col] = "industry"
        
        df = df.rename(columns=col_map)
        df["ts_code"] = df["ts_code"].astype(str).str.zfill(6)
        return df
    except Exception as e:
        print(f"[WARN] 涨停池获取失败: {e}", file=sys.stderr)
        return pd.DataFrame()


def fetch_dragon_tiger(trade_date: str) -> pd.DataFrame:
    """获取龙虎榜数据"""
    try:
        time.sleep(0.5)
        df = ak.stock_lhb_detail_em(date=trade_date)
        if df is None or df.empty:
            return pd.DataFrame()
        
        col_map = {}
        for col in df.columns:
            if "代码" in col:
                col_map[col] = "ts_code"
            elif "名称" in col:
                col_map[col] = "name"
            elif "收盘价" in col:
                col_map[col] = "close"
            elif "涨跌幅" in col:
                col_map[col] = "pct_chg"
            elif "原因" in col:
                col_map[col] = "reason"
            elif "净买额" in col or "净买入" in col:
                col_map[col] = "net_amount"
            elif "买入额" in col:
                col_map[col] = "buy_amount"
            elif "卖出额" in col:
                col_map[col] = "sell_amount"
            elif "营业部" in col or "席位" in col:
                col_map[col] = "seat"
        
        df = df.rename(columns=col_map)
        df["ts_code"] = df["ts_code"].astype(str).str.zfill(6)
        return df
    except Exception as e:
        print(f"[WARN] 龙虎榜获取失败: {e}", file=sys.stderr)
        return pd.DataFrame()


def fetch_sector_info(trade_date: str) -> pd.DataFrame:
    """获取板块涨跌数据(用于判断板块共振)"""
    try:
        time.sleep(0.5)
        df = ak.stock_board_industry_name_em()
        if df is None or df.empty:
            return pd.DataFrame()
        
        col_map = {}
        for col in df.columns:
            if "板块名称" in col:
                col_map[col] = "sector_name"
            elif "涨跌幅" in col:
                col_map[col] = "pct_chg"
            elif "上涨家数" in col:
                col_map[col] = "up_count"
            elif "下跌家数" in col:
                col_map[col] = "down_count"
            elif "领涨股票" in col:
                col_map[col] = "lead_stock"
        
        df = df.rename(columns=col_map)
        return df
    except Exception as e:
        print(f"[WARN] 板块数据获取失败: {e}", file=sys.stderr)
        return pd.DataFrame()


def fetch_market_overview(trade_date: str) -> dict:
    """获取市场整体数据(涨跌停家数等)"""
    try:
        time.sleep(0.5)
        df = ak.stock_zh_a_spot_em()
        if df is None or df.empty:
            return {}
        
        total = len(df)
        up_count = len(df[df["涨跌幅"] > 0])
        down_count = len(df[df["涨跌幅"] < 0])
        limit_up_count = len(df[df["涨跌幅"] >= 9.9])
        limit_down_count = len(df[df["涨跌幅"] <= -9.9])
        
        return {
            "trade_date": trade_date,
            "total_stocks": total,
            "up_count": up_count,
            "down_count": down_count,
            "limit_up_count": limit_up_count,
            "limit_down_count": limit_down_count,
            "up_ratio": round(up_count / total * 100, 1) if total > 0 else 0,
            "limit_ratio": round(limit_up_count / total * 100, 2) if total > 0 else 0,
        }
    except Exception as e:
        print(f"[WARN] 市场概览获取失败: {e}", file=sys.stderr)
        return {}


def safe_serialize(obj):
    """JSON序列化处理NaN"""
    if isinstance(obj, float):
        if pd.isna(obj) or pd.isinf(obj):
            return None
        return round(obj, 4)
    if isinstance(obj, (pd.Timestamp, datetime)):
        return obj.strftime("%Y-%m-%d %H:%M:%S")
    if isinstance(obj, date):
        return obj.strftime("%Y-%m-%d")
    return obj


def main():
    parser = argparse.ArgumentParser(description="涨停股数据采集工具")
    parser.add_argument("date", nargs="?", default=None, help="交易日期(YYYYMMDD)，默认最近交易日")
    parser.add_argument("--output", "-o", action="store_true", help="输出JSON到文件")
    parser.add_argument("--outdir", type=str, default=None, help="输出目录")
    args = parser.parse_args()

    trade_date = args.date or get_last_trading_day()
    print(f"正在采集 {trade_date} 涨停数据...", file=sys.stderr)

    # 1. 市场概览
    market = fetch_market_overview(trade_date)
    print(f"  市场概览: 涨停{market.get('limit_up_count', '?')}家 / 跌停{market.get('limit_down_count', '?')}家", file=sys.stderr)

    # 2. 涨停池
    limit_pool = fetch_limit_pool(trade_date)
    print(f"  涨停池: {len(limit_pool)} 只", file=sys.stderr)

    # 3. 龙虎榜
    lhb = fetch_dragon_tiger(trade_date)
    print(f"  龙虎榜: {len(lhb)} 条", file=sys.stderr)

    # 4. 板块数据
    sectors = fetch_sector_info(trade_date)
    print(f"  板块数据: {len(sectors)} 个行业", file=sys.stderr)

    # 构建输出
    result = {
        "trade_date": trade_date,
        "market": market,
        "limit_up_stocks": [],
        "dragon_tiger": [],
        "hot_sectors": [],
    }

    # 涨停股列表
    if not limit_pool.empty:
        for _, row in limit_pool.iterrows():
            stock = {}
            for k, v in row.items():
                stock[k] = safe_serialize(v)
            result["limit_up_stocks"].append(stock)

    # 龙虎榜
    if not lhb.empty:
        for _, row in lhb.iterrows():
            item = {}
            for k, v in row.items():
                item[k] = safe_serialize(v)
            result["dragon_tiger"].append(item)

    # 热门板块(涨幅前20)
    if not sectors.empty:
        pct_col = [c for c in sectors.columns if "pct_chg" in c]
        if pct_col:
            top_sectors = sectors.nlargest(20, pct_col[0])
            for _, row in top_sectors.iterrows():
                sector = {}
                for k, v in row.items():
                    sector[k] = safe_serialize(v)
                result["hot_sectors"].append(sector)

    # 输出JSON
    json_str = json.dumps(result, ensure_ascii=False, indent=2, default=str)

    if args.output:
        outdir = Path(args.outdir) if args.outdir else Path(".")
        outdir.mkdir(parents=True, exist_ok=True)
        outpath = outdir / f"limit_up_{trade_date}.json"
        outpath.write_text(json_str, encoding="utf-8")
        print(f"\n数据已保存到: {outpath}", file=sys.stderr)
    else:
        print(json_str)


if __name__ == "__main__":
    main()
