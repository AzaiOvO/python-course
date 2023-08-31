import React, { useRef } from 'react';
import axios from 'axios';
import * as echarts from 'echarts';

export default function House() {
    const myChart = useRef();

    React.useEffect(() => {
        axios.get("http://localhost:3000/api/house").then(res => {
            const data_receive = res.data
            // data_receive.forEach(element => {
            //     var obj = JSON.parse(element)
            //     data.push(obj)
            // });
            // console.log(data_receive);
            let myChart_Instance = echarts.init(myChart.current)

            let option = {
                title: {
                    text: '房源户型（室）的数量统计图',
                    left: 'center'
                },
                tooltip: {
                    trigger: 'item'
                },
                legend: {
                    top: '5%',
                    left: 'center'
                },
                series: [
                    {
                        name: '数量',
                        type: 'pie',
                        radius: ['40%', '70%'],
                        avoidLabelOverlap: false,
                        itemStyle: {
                            borderRadius: 10,
                            borderColor: '#fff',
                            borderWidth: 2
                        },
                        label: {
                            show: false,
                            position: 'center'
                        },
                        emphasis: {
                            label: {
                                show: true,
                                fontSize: 40,
                                fontWeight: 'bold'
                            }
                        },
                        labelLine: {
                            show: false
                        },
                        data: [
                            { value: data_receive.s1, name: '1室' },
                            { value: data_receive.s2, name: '2室' },
                            { value: data_receive.s3, name: '3室' },
                            { value: data_receive.s4, name: '4室' },
                            { value: data_receive.s5, name: '5室' },
                            { value: data_receive.s6, name: '6室' },
                            { value: data_receive.s8, name: '8室' }
                        ]
                    }
                ]
            };

            myChart_Instance.setOption(option)
        })
    })

    return (
        <div style={{ textAlign: "center" }}>
            <div className='echarts' ref={myChart} style={{ height: "600px" }} />
        </div>

    )
}
