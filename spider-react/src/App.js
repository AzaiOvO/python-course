import './App.css';
import React from 'react'
import { Route, Routes } from 'react-router-dom';
import Main from './component/Main/main'

function App() {
  return (
    <div>
      {/* 注册路由（路由表写法） */}
      {/* {element} */}
      <Routes>
        <Route path='/' element={<Main />} />
        <Route path='/main/*' element={<Main />} />
      </Routes>

    </div>
  );
}

export default App;
