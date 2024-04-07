import MainNavItem from "../main-nav-item/MainNavItem.jsx"
import styles from "./MainNav.module.css"
import listIcon from "../../assets/list.png"
import auctionHammerIcon from "../../assets/auction-hammer.png"
import userIcon from "../../assets/user.png"

function MainNav() {

    const navItemsData = [
        {
            "id": 1,
            "icon": listIcon,
            "alternativeText": "Ícone de uma lista"
        },
        {
            "id": 2,
            "icon": auctionHammerIcon,
            "alternativeText": "Ícone de um martelo de leilão"
        },
        {
            "id": 3,
            "icon": userIcon,
            "alternativeText": "Ícone de usuário"
        }
    ]

    const navItemsComponents = navItemsData.map((item) => {
        return <MainNavItem key={item.id} icon={item.icon} alternativeText={item.alternativeText}/>
    })

    return (
        <aside className={styles.aside}>
            <nav>
                <ul className={styles.liContainer}>
                    {navItemsComponents}
                </ul>
            </nav>
        </aside>
    )
}

export default MainNav;