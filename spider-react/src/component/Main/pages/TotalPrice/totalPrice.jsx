import React, { useRef } from 'react';
import axios from 'axios';
import * as echarts from 'echarts';

export default function TotalPrice() {
    const myChart = useRef();

    React.useEffect(() => {
        axios.get("http://localhost:3000/api/total_price").then(res => {
            const data_receive = res.data
            // data_receive.forEach(element => {
            //     var obj = JSON.parse(element)
            //     data.push(obj)
            // });
            // console.log(data_receive);
            let myChart_Instance = echarts.init(myChart.current)

            myChart_Instance.setOption({
                title: {
                    text: '房源总价的数量统计图',
                    left: 'center'
                },
                xAxis: {
                    type: 'category',
                    data: ['80万以下', '80-100万', '100-120万', '120-150万', '150-200万', '200-300万', '300-500万', '500万以上']
                },
                yAxis: {
                    type: 'value'
                },
                series: [
                    {
                        data: [data_receive.below_80w,
                        data_receive.w80_100,
                        data_receive.w100_120,
                        data_receive.w120_150,
                        data_receive.w150_200,
                        data_receive.w200_300,
                        data_receive.w300_500,
                        data_receive.up_500w,],
                        type: 'line',
                        symbol: 'triangle',
                        symbolSize: 20,
                        lineStyle: {
                            color: '#5470C6',
                            width: 4,
                            type: 'dashed'
                        },
                        itemStyle: {
                            borderWidth: 3,
                            borderColor: '#EE6666',
                            color: 'yellow'
                        },
                        label: {
                            normal: {
                                show: true,//开启显示
                                position: 'top',//柱形上方
                                textStyle: { //数值样式
                                    color: '#000000'
                                }
                            }
                        }
                    },

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
