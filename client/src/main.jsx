import React from 'react'
import ReactDOM from 'react-dom/client'
import './index.css'

import { createBrowserRouter, RouterProvider } from "react-router-dom"
import Home from './pages/Home'
import SignIn from './pages/SignIn'
import SignUp from './pages/SignUp'
import ListOfAuctions from './pages/ListOfAuctions'
import Auction from './pages/Auction'
import MyAuctions from './pages/MyAuctions'
import NewAuction from './pages/NewAuction'
import Me from './pages/Me'
import PersonalData from './pages/PersonalData'

const router = createBrowserRouter([
  {
    path: "/",
    element: <Home />
  },
  {
    path: "/sign-in",
    element: <SignIn />
  },
  {
    path: "/sign-up",
    element: <SignUp />
  },
  {
    path: "/list-auctions",
    element: <ListOfAuctions />
  },
  {
    path: "/auctions/:id",
    element: <Auction />
  },
  {
    path: "/my-auctions/",
    element: <MyAuctions />
  },
  {
    path: "/new-auction",
    element: <NewAuction />
  },
  {
    path: "/me",
    element: <Me />,
    children: [
      {
        path:"/me/personal-data",
        element: <PersonalData />
      }
    ]
  }

])

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>,
)
