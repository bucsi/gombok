import delegate from "./delegate.js"

async function handleBtnClick(ev, target) {
    const mod1 = target.dataset.mod1
    const mod2 = target.dataset.mod2
    const key = target.dataset.key
    console.log(`Sending keypresses to the server: ${mod1} ${mod2} ${key}`)
    const URL = window.location.href + "/press"
    await fetch(URL + `?mod1=${mod1}&mod2=${mod2}&key=${key}`)
}

const btns = document.querySelectorAll("button")
delegate(document, "button", "click", handleBtnClick)
