import MainHeader from "../main-header/MainHeader.jsx"
import MainNav from "../main-nav/MainNav.jsx"
import MainWrapper from "../main-wrapper/MainWrapper.jsx"

function MainLayout(props) {

  return (
    <>
      <MainHeader />
      <MainWrapper>
        <MainNav />
        {props.children}
      </MainWrapper>
    </>
  )
}

export default MainLayout
