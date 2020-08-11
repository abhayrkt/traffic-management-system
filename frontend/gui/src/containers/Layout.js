import React from'react';
import { Layout, Menu, Breadcrumb } from 'antd';
import { Link } from 'react-router-dom';

const { Header, Content, Footer } = Layout;

const CustomLayout = (props) => {
    return (
                <Layout className="layout">
                <Header>
                <div className="logo" />
                <Menu theme="dark" mode="horizontal" defaultSelectedKeys={['2']}>
                    <Menu.Item key="1"><b>Reviews</b></Menu.Item>
                    
                </Menu>
                </Header>
                <Content style={{ padding: '0 50px' }}>
                <Breadcrumb style={{ margin: '16px 0' }}>
                    <Breadcrumb.Item><Link to="/"><b>Home</b></Link></Breadcrumb.Item>
                    
                </Breadcrumb>
                <div className="site-layout-content">
                    {props.children}
                </div>
                </Content>
                <Footer style={{ textAlign: 'center' }}>PES UNIVERSITY ELECTRONIC CITY CAMPUS</Footer>
            </Layout>
    
    ); 
}


export default CustomLayout;

  