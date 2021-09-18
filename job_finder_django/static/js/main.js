// ALERTS

document.querySelectorAll('.toast__close').forEach(item => {
    item.addEventListener('click', (e) => {
        let parent = (e.target).closest('.toast');
        parent.remove()
    })
})