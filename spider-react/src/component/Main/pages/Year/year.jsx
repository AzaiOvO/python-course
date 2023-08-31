import React, { useRef } from 'react';
import axios from 'axios';
import * as echarts from 'echarts';

export default function Year() {
    const myChart = useRef();

    React.useEffect(() => {
        axios.get("http://localhost:3000/api/year").then(res => {
            // let data = []
            const data_receive = res.data
            // data_receive.forEach(element => {
            //     var obj = JSON.parse(element)
            //     data.push(obj)
            // });
            data_receive[0].year = '年份不详'
            // console.log(data_receive);
            let myChart_Instance = echarts.init(myChart.current)

            myChart_Instance.setOption({
                title: {
                    text: '房源建造年份数量统计图',
                    left: 'center'
                },
                xAxis: {
                    type: 'category',
                    data: data_receive.map((item) => {
                        return item.year
                    })
                },
                yAxis: {
                    type: 'value'
                },
                series: [
                    {
                        data: data_receive.map((item) => {
                            return item.count
                        }),
                        type: 'bar',
                        showBackground: true,
                        backgroundStyle: {
                            color: 'rgba(180, 180, 180, 0.2)'
                        },
                        label: {
                            normal: {
                                show: true,//开启显示
                                position: 'top',//柱形上方
                                textStyle: { //数值样式
                                    color: '#ed371b'
                                }
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
