import React, { useRef } from 'react';
import axios from 'axios';
import * as echarts from 'echarts';

export default function Price() {
    const myChart = useRef();

    React.useEffect(() => {
        axios.get("http://localhost:3000/api/price").then(res => {
            const data_receive = res.data
            // data_receive.forEach(element => {
            //     var obj = JSON.parse(element)
            //     data.push(obj)
            // });
            // console.log(data_receive);
            let myChart_Instance = echarts.init(myChart.current)

            myChart_Instance.setOption({
                title: {
                    text: '房源每平价格区间的数量统计图',
                    left: 'center'
                },
                xAxis: {
                    type: 'category',
                    data: ['1万以下', '1-2万', '2-3万', '3-4万', '4-5万', '5万以上']
                },
                yAxis: {
                    type: 'value'
                },
                series: [
                    {
                        data: [data_receive.below_1w,
                        data_receive.w1_2,
                        data_receive.w2_3,
                        data_receive.w3_4,
                        data_receive.w4_5,
                        data_receive.up_5w,],
                        type: 'line',
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
