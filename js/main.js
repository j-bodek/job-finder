// SEARCH

const inputField = document.querySelector('.chosen-value');
const dropdown = document.querySelector('.value-list');
const dropdownArray = [...document.querySelectorAll('li')];
let valueArray = [];
dropdownArray.forEach(item => {
    valueArray.push(item.textContent);
});

const closeDropdown = () => {
    dropdown.classList.add('closed');
}

inputField.addEventListener('input', () => {
    dropdown.classList.add('open');
    let inputValue = inputField.value.toLowerCase();
    let valueSubstring;
    if (inputValue.length > 0) {
        for (let j = 0; j < valueArray.length; j++) {
            if (!(inputValue.substring(0, inputValue.length) === valueArray[j].substring(0, inputValue.length).toLowerCase())) {
                dropdownArray[j].classList.add('closed');
            } else {
                dropdownArray[j].classList.remove('closed');
            }
        }
    } else {
        for (let i = 0; i < dropdownArray.length; i++) {
            dropdownArray[i].classList.remove('closed');
        }
    }
});

dropdownArray.forEach(item => {
    item.addEventListener('click', (evt) => {
        inputField.value = item.textContent;
        dropdownArray.forEach(dropdown => {
            dropdown.classList.remove('closed');
        });
    });
})

inputField.addEventListener('focus', () => {
    inputField.placeholder = 'Type to filter';
    dropdown.classList.add('open');
    dropdownArray.forEach(dropdown => {
        dropdown.classList.remove('closed');
    });
});

inputField.addEventListener('blur', () => {
    inputField.placeholder = 'Search Industry';
    dropdown.classList.remove('open');
});

document.addEventListener('click', (evt) => {
    const isDropdown = dropdown.contains(evt.target);
    const isInput = inputField.contains(evt.target);
    if (!isDropdown && !isInput) {
        dropdown.classList.remove('open');
    }
});


// SKILLS
let skill_bar = document.getElementById('skill_bar')
let skills_list = document.getElementById('skills')

skill_bar.addEventListener('keypress', (e) => {
    if (e.key == 'Enter') {
        let new_skill = document.createElement("li");
        new_skill.setAttribute("id", skill_bar.value);
        new_skill.setAttribute("class", 'skill');
        new_skill.innerHTML = `${skill_bar.value} &#215;`
        skills_list.appendChild(new_skill)
        skill_bar.value = ''
    }
})




skills_list.addEventListener('click', (e) => {
    let skill = e.target
    if (skill.className == 'skill') {
        skill.remove()
    }
})