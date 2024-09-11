import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import MatrixChatPage from './App';
import reportWebVitals from './reportWebVitals';

// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyBEHcZj2RrUJIPP-IN8P-tt9Dpp88lPKJ0",
  authDomain: "reorganism-in-app.firebaseapp.com",
  projectId: "reorganism-in-app",
  storageBucket: "reorganism-in-app.appspot.com",
  messagingSenderId: "1012963969564",
  appId: "1:1012963969564:web:89b853e6fdbf22e2732dd9",
  measurementId: "G-HETBSVQ8K2"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <MatrixChatPage />
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
