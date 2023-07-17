import React, { Component } from "react";
import { Route, Routes } from "react-router-dom";
import HomePage from "./Components/HomePage/HomePage";
import Layout from "./Components/Layout/Layout";

const routes = [{ path: "/", Component: HomePage }];

const AllRoutes = () => {
  return (
    <Layout>
      <Routes>
        {routes.map((route, index) => (
          <Route
            key={index}
            path={route.path}
            element={<route.Component />}
          ></Route>
        ))}
      </Routes>
    </Layout>
  );
};

export default AllRoutes;
