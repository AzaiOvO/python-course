import React, { useRef } from 'react';
import axios from 'axios';
import * as echarts from 'echarts';

export default function Area() {
    const myChart = useRef();

    React.useEffect(() => {
        axios.get("http://localhost:3000/api/area").then(res => {
            const data_receive = res.data
            // data_receive.forEach(element => {
            //     var obj = JSON.parse(element)
            //     data.push(obj)
            // });
            // console.log(data_receive);
            let myChart_Instance = echarts.init(myChart.current)

            myChart_Instance.setOption({
                title: {
                    text: '房源面积的数量统计图',
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
                            { value: data_receive['below_50'], name: '50m²以下' },
                            { value: data_receive['a50-70'], name: '50-70m²' },
                            { value: data_receive['a70-90'], name: '70-90m²' },
                            { value: data_receive['a90-110'], name: '90-110m²' },
                            { value: data_receive['a110-130'], name: '110-130m²' },
                            { value: data_receive['a130-150'], name: '130-150m²' },
                            { value: data_receive['a150-200'], name: '150-200m²' },
                            { value: data_receive['up_200'], name: '200m²以上' }
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
