import React, { useRef } from 'react';
import axios from 'axios';
import * as echarts from 'echarts';

export default function Floor() {
    const myChart = useRef();

    React.useEffect(() => {
        axios.get("http://localhost:3000/api/floor").then(res => {
            const data_receive = res.data
            // data_receive.forEach(element => {
            //     var obj = JSON.parse(element)
            //     data.push(obj)
            // });
            console.log(data_receive);
            let myChart_Instance = echarts.init(myChart.current)

            myChart_Instance.setOption({
                title: {
                    text: '房源所在层分类数量统计图',
                    left: 'center'
                },
                tooltip: {
                    trigger: 'item'
                },
                legend: {
                    orient: 'vertical',
                    left: 'left'
                },
                series: [
                    {
                        name: '数量',
                        type: 'pie',
                        radius: '50%',
                        data: [
                            { value: data_receive['level_1'], name: '底层' },
                            { value: data_receive['level_2'], name: '低层' },
                            { value: data_receive['level_3'], name: '中层' },
                            { value: data_receive['level_4'], name: '高层' },
                            { value: data_receive['level_5'], name: '顶层' },
                        ],
                        emphasis: {
                            itemStyle: {
                                shadowBlur: 10,
                                shadowOffsetX: 0,
                                shadowColor: 'rgba(0, 0, 0, 0.5)'
                            }
                        }
                    }
                ]
            })
        })
    })

    return (
        <div style={{ textAlign: "center" }}>
            <div className='echarts' ref={myChart} style={{ height: "600px" }} />
        </div>

    )
}
