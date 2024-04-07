import styles from "./MainNavItem.module.css"

function MainNavItem(props) {
    return (
        <li className={styles.divCircle}>
            <img src={props.icon} alt={props.alternativeText} className={styles.img} />
        </li>
    )
}

export default MainNavItem;