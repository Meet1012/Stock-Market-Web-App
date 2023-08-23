import React, { useContext, useState, useEffect } from 'react'
import {
    Area,
    AreaChart,
    ResponsiveContainer,
    Tooltip,
    XAxis,
    YAxis
} from "recharts";
import { convertUnixTimestamptoDate } from '../helpers/date-helper';
import { convertDatetoUnixTimestamp } from '../helpers/date-helper';
import { createDate } from '../helpers/date-helper';
import Card from './Card';
import ChartFilter from './ChartFilter';
import { chartConfig } from '../constant/config';
import ThemeContext from '../context/ThemeContext';
import { fetchHistoricalData } from '../api/local-api';
// import { fetchHistoricalData } from '../api/alphavantage-api';
import StockContext from '../context/StockContext';
// import { mockHistoricalData } from '../constant/mock';

const Chart = () => {
    const [data, setData] = useState({});
    const [filter, setFilter] = useState("1W");

    const { darkMode } = useContext(ThemeContext);
    const { stockSymbol } = useContext(StockContext);



    useEffect(() => {
        const getDateRange = () => {
            const { days, weeks, months, years } = chartConfig[filter];

            const endDate = new Date();
            const startDate = createDate(endDate, -days, -weeks, -months, -years);

            const startTimestampUnix = convertDatetoUnixTimestamp(startDate);
            const endTimestampUnix = convertDatetoUnixTimestamp(endDate);

            return { startTimestampUnix, endTimestampUnix };
        };
        const UpdateChartData = async () => {
            try {
                const { startTimestampUnix, endTimestampUnix } = getDateRange();
                const resolution = chartConfig[filter].resolution;
                const result = await fetchHistoricalData(stockSymbol, resolution, startTimestampUnix, endTimestampUnix);
                setData(formatData(result));
            }
            catch (error) {
                setData([]);
                console.log(error);
            }
        };

        UpdateChartData();
    }, [stockSymbol, filter]);

    const formatData = (data) => {
        console.log(data.c);
        return data.c.map((item, index) => {
            return {
                value: item.toFixed(2),
                date: convertUnixTimestamptoDate(data.t[index])
                
            };
        });
    };

    

    return (
        <Card>
            {/* <ul className='flex absolute top-2 right-2 z-40'>
                {Object.keys(chartConfig).map((item) => {
                    return (
                        <li key={item}>
                            <ChartFilter text={item} active={filter === item} onClick={() => {
                                setFilter(item);
                            }} />
                        </li>)
                })}
            </ul> */}
            <ResponsiveContainer>
                <AreaChart data={data}>
                    <defs>
                        <linearGradient id='chartColor' x1="0" y1="0" x2="0" y2="1">
                            <stop offset="5%" stopColor={darkMode ? "#312e81" : "rgb(199 210 254"} stopOpacity={0.8}></stop>
                            <stop offset="95%" stopColor={darkMode ? "#312e81" : "rgb(199 210 254"} stopOpacity={0}></stop>
                        </linearGradient>
                    </defs>
                    <Area type="monotone" dataKey="value" stroke="#312e81" fillOpacity={1}
                        strokeWidth={0.5}
                        fill='url(#chartColor)' />
                    <Tooltip contentStyle={darkMode ? { backgroundColor: "#111827" } : null}
                        itemStyle={darkMode ? { color: "#818cf8" } : null} />
                    <XAxis dataKey={"date"} />
                    <YAxis domain={['dataMin - 50', 'dataMax + 50']} />
                </AreaChart>
            </ResponsiveContainer>
        </Card>
    )
}

export default Chart