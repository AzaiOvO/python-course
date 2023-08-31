import React from 'react';
import { InputNumber, Table, Button } from 'antd';
import { SearchOutlined } from '@ant-design/icons'
import { Component } from 'react';
import axios from 'axios';
import './list.css'
//需要的数据类型
const columns = [
    {
        title: '房源名称',
        dataIndex: 'name',
        key: 'name',
        render: (text, record) => {
            return <a href={record.link}> {text}</a >
        },
    },
    {
        title: '户型（室）',
        dataIndex: 'house',
        key: 'house',
        sorter: (a, b) => a.house - b.house,
    },
    {
        title: '户型（厅）',
        dataIndex: 'hall',
        key: 'hall',
    },
    {
        title: '面积/㎡',
        dataIndex: 'area',
        key: 'area',
        sorter: (a, b) => a.area - b.area,
    },
    {
        title: '所在楼层（高底层）',
        dataIndex: 'floor',
        key: 'floor',
    },
    {
        title: '所在楼所有层数',
        dataIndex: 'count_floor',
        key: 'count_floor',
    },
    {
        title: '朝向',
        dataIndex: 'toward',
        key: 'toward',
    },
    {
        title: '建造年份',
        dataIndex: 'year',
        key: 'year',
        sorter: (a, b) => a.year - b.year,
    },
    {
        title: '房源中介人',
        dataIndex: 'intermediary_agent',
        key: 'intermediary_agent',
    },
    {
        title: '小区名',
        dataIndex: 'developers',
        key: 'developers',
    },
    {
        title: '地址',
        dataIndex: 'address',
        key: 'address',
    },
    {
        title: '备注',
        dataIndex: 'remark',
        key: 'remark',
    },
    {
        title: '总房价(万元)',
        dataIndex: 'total_price',
        key: 'total_price',
        sorter: (a, b) => a.total_price - b.total_price,
    },
    {
        title: '每平方单价(元/㎡)',
        dataIndex: 'price',
        key: 'price',
        sorter: (a, b) => a.price - b.price,
    },
];


export default class List extends Component {

    state = {
        data: [],
        area1: 0,
        area2: 0,
        price1: 0,
        price2: 0,
    }

    UNSAFE_componentWillMount() {
        //axios异步获取数据
        axios.get("http://localhost:3000/api/list").then(res => {
            let data = []
            const data_receive = res.data
            data_receive.forEach(element => {
                var obj = JSON.parse(element)
                obj.link = 'https://nanjing.esf.fang.com' + obj.link
                data.push(obj)
            });
            this.setState({ data: data })
        })
    }

    componentDidMount() {

    }
    componentWillUnmount() {
    }

    searchByArea = () => {
        // console.log(this.state);
        const area1 = this.state.area1
        const area2 = this.state.area2
        if (area1 > area2) {
            alert("后面数字要比前面大！")
        }
        const area = { 'area1': area1, 'area2': area2 }
        axios.post("http://localhost:3000/api/search_by_area", area).then(
            response => {
                let data = []
                const data_receive = response.data
                if (data_receive === 'error') {
                    alert("输入有误,请重新检查输入！")
                } else {
                    data_receive.forEach(element => {
                        var obj = JSON.parse(element)
                        obj.link = 'https://nanjing.esf.fang.com' + obj.link
                        data.push(obj)
                    });
                    this.setState({ data: data })
                    alert("查询完成，数据已更新！")
                }
            })
    }

    searchByPrice = () => {
        // console.log(this.state);
        const price1 = this.state.price1
        const price2 = this.state.price2
        if (price1 > price2) {
            alert("后面数字要比前面大！")
        }
        const price = { 'price1': price1, 'price2': price2 }
        axios.post("http://localhost:3000/api/search_by_price", price).then(
            response => {
                let data = []
                const data_receive = response.data
                if (data_receive === 'error') {
                    alert("输入有误,请重新检查输入！")
                } else {
                    data_receive.forEach(element => {
                        var obj = JSON.parse(element)
                        obj.link = 'https://nanjing.esf.fang.com' + obj.link
                        data.push(obj)
                    });
                    this.setState({ data: data })
                    alert("查询完成，数据已更新！")
                }
            })
    }

    render() {
        const data = this.state.data

        return (
            <div>
                <div className='div_main'>
                    <div className="div_number">
                        <p className='p_number'>根据面积查询：</p>
                        <InputNumber id='input1' controls={false} className='inputNumber' onChange={(number) => {
                            this.setState({ area1: number })
                        }} />
                        <p className='p_number'>-</p>
                        <InputNumber id='input2' controls={false} className='inputNumber' onChange={(number) => {
                            this.setState({ area2: number })
                        }}>
                        </InputNumber>
                        <h3 className='p_number'>㎡</h3>
                        <Button type="primary" icon={<SearchOutlined />} onClick={this.searchByArea}>
                            Search
                        </Button>
                    </div>
                    <div className="div_price" >
                        <p className='p_number'>根据总价查询：</p>
                        <InputNumber controls={false} className='inputNumber' onChange={(number) => {
                            this.setState({ price1: number })
                        }} />
                        <p className='p_number'>-</p>
                        <InputNumber controls={false} className='inputNumber' onChange={(number) => {
                            this.setState({ price2: number })
                        }}>
                        </InputNumber>
                        <h3 className='p_number'>万元</h3>
                        <Button type="primary" icon={<SearchOutlined />} onClick={this.searchByPrice}>
                            Search
                        </Button>
                    </div>
                </div>

                <div>
                    <Table dataSource={data}
                        columns={columns}
                        pagination={{ position: 'bottomRight' }}
                        defaultExpandAllRows={true}
                        size='large'
                        bordered='true'
                        scroll={{ y: 550 }}
                    />
                </div>
            </div>
        )
    }
}
