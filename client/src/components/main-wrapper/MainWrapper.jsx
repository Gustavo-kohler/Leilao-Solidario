import styles from "./MainWrapper.module.css"

function MainWrapper(props) {
    return (
        <div className={styles.mainWrapper}>
            {props.children}
        </div>
    )
}

export default MainWrapper;