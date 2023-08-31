import React, { useState } from 'react';
import './main'
import List from './pages/List/list'
import Area from './pages/Area/area'
import House from './pages/House/house'
import Floor from './pages/Floor/floor'
import Year from './pages/Year/year'
import Price from './pages/Price/price'
import TotalPrice from './pages/TotalPrice/totalPrice'

import {
    BarChartOutlined,
    HistoryOutlined,
    OrderedListOutlined,
    PieChartOutlined,
    MoneyCollectOutlined
} from '@ant-design/icons';
import { Breadcrumb, Layout, Menu, theme } from 'antd';
import { Route, Routes, useNavigate } from 'react-router-dom';
const { Header, Content, Footer, Sider } = Layout;
function getItem(label, key, icon, children) {
    return {
        key,
        icon,
        children,
        label,
    };
}
const items = [
    getItem('房源列表', '1', <OrderedListOutlined />),
    getItem('面积统计', '2', <PieChartOutlined />),
    getItem('户型统计', 'sub1', <BarChartOutlined />, [
        getItem('按室数统计', '3'),
        getItem('按楼层统计', '4'),
        // getItem('按朝向统计', '5'),
    ]),
    getItem('价格统计', 'sub2', <MoneyCollectOutlined />, [getItem('每平价格', '5'), getItem('总价统计', '6')]),
    getItem('年份统计', '7', <HistoryOutlined />),
];

const Main = () => {
    const navigate = useNavigate()
    const [collapsed, setCollapsed] = useState(false);

    const {
        token: { colorBgContainer },
    } = theme.useToken();

    function jump(item) {
        switch (item.key) {
            case '1':
                navigate('/main/list')
                break
            case '2':
                navigate('/main/area')
                break
            case '3':
                navigate('/main/house')
                break
            case '4':
                navigate('/main/floor')
                break
            case '5':
                navigate('/main/price')
                break
            case '6':
                navigate('/main/totalPrice')
                break
            case '7':
                navigate('/main/year')
                break
            default:
                navigate('/main')
                break
        }
    }

    return (
        <Layout
            style={{
                minHeight: '100vh',
            }}
        >
            <Sider collapsible collapsed={collapsed} onCollapse={(value) => setCollapsed(value)}>
                <div className="demo-logo-vertical" />
                <Menu theme="dark" defaultSelectedKeys={['1']} mode="inline" items={items} onClick={jump}>
                    {/* <Menu.Item>
                        <PieChartOutlined key="1"><Link to='/main/test'>测试！</Link></PieChartOutlined>
                    </Menu.Item> */}
                </Menu>
            </Sider>
            <Layout>
                <Header
                    style={{
                        padding: 0,
                        background: colorBgContainer,
                    }}>
                    <h2 style={{ margin: '0 16px', }}>房源数据可视化系统</h2>
                </Header>
                <Content
                    style={{
                        margin: '0 16px',
                    }}
                >
                    <Breadcrumb
                        style={{
                            margin: '16px 0',
                        }}
                    >
                        <Breadcrumb.Item> </Breadcrumb.Item>
                    </Breadcrumb>
                    <div
                        style={{
                            padding: 24,
                            minHeight: 360,
                            background: colorBgContainer,
                        }}
                    >
                        <Routes>
                            <Route path='list' element={<List />} />
                            <Route path='area' element={<Area />} />
                            <Route path='house' element={<House />} />
                            <Route path='floor' element={<Floor />} />
                            <Route path='year' element={<Year />} />
                            <Route path='price' element={<Price />} />
                            <Route path='totalPrice' element={<TotalPrice />} />
                        </Routes>
                    </div>
                </Content>
                <Footer
                    style={{
                        textAlign: 'center',
                    }}
                >
                    {/* <a href='https://github.com/AzaiOvO/python-course'>本人Github主页</a> */}
                </Footer>
            </Layout>
        </Layout>
    );
};

export default Main