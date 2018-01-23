import React from "react";
import ReactDOM from "react-dom";
import "index.css";
import App from "App";
import { Provider } from "react-redux";
import configureStore from "redux/configureStore";

const store = configureStore();
console.log(store.getState())
ReactDOM.render(
  <Provider store={store}>
    <App />
  </Provider>,
  document.getElementById("root")
);