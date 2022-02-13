/**
 *
 * @param {Node} parent the HTML element to which the delegate will be attached.
 * @param {keyof HTMLElementTagNameMap} child a CSS selector, describing intended targets of the delegate.
 * @param {string} when an event name, e.g. 'click' or 'mouseover', when the delegate will run.
 * @param {(ev: Event, target: Node) => null} what the delegated function.
 */
export default function delegate(parent, child, when, what) {
    function eventHandler(ev) {
        const eventsTarget = ev.target
        const eventsHandler = this
        const closestMachingElement = eventsTarget.closest(child)

        if (eventsHandler.contains(closestMachingElement)) {
            what(ev, closestMachingElement)
        }
    }

    parent.addEventListener(when, eventHandler)
}
