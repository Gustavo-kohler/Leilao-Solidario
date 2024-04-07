import styles from "./MainHeader.module.css"
import logoIpsum from "../../assets/logoipsum.svg"

function MainHeader() {

    const altTextLogo = "Logo do Leilão Solidário"

    return (
        <header className={styles.header}>
            <img src={logoIpsum} alt={altTextLogo} />
        </header>
    )
}

export default MainHeader;