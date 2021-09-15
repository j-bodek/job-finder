// SEARCH

const inputField = document.querySelectorAll('.chosen-value');
const dropdown = document.querySelectorAll('.value-list');
// const dropdownArray = [...document.querySelectorAll('li')];


let returnValueArray = (dropdownArray) => {
    let valueArray = [];
    dropdownArray.forEach(item => {
        valueArray.push(item.textContent);
    });
    return valueArray
}


const closeDropdown = () => {
    dropdown.classList.add('closed');
}


inputField.forEach(input => {
    input.addEventListener('input', () => {
        let label = input.closest("label");
        let dropdown = label.querySelector('.value-list')

        let dropdownArray = label.querySelectorAll('.dropdown_items')
        let valueArray = returnValueArray(dropdownArray)

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
})



inputField.forEach(input => {
    input.addEventListener('click', (e) => {
        let label = input.closest("label");
        let dropdown = label.querySelector('.value-list')
        inputField.placeholder = 'Type to filter';
        dropdown.classList.add('open');
        let dropdownArray = label.querySelectorAll('.dropdown_items')
        dropdownArray.forEach(dropdown => {
            dropdown.classList.remove('closed');
        });


    });
})




dropdown.forEach(list => {
    list.addEventListener('click', (e) => {
        let input = list.closest("label").querySelector('.chosen-value');
        displayChoosenValue(e.target, input)
    })
})



let displayChoosenValue = (item, input) => {
    if (input.id !== 'skill_bar') {
        input.value = item.textContent;
    } else {
        input.value = item.textContent;
        appendSkill(input)
        input.value = '';
    }
}



inputField.forEach(input => {
    input.addEventListener('blur', () => {
        inputField.placeholder = 'Search Industry';
        let label = input.closest("label");
        let dropdown = label.querySelector('.value-list')
        dropdown.classList.remove('open');
    });
})







// SKILLS
let skill_bar = document.getElementById('skill_bar')
let skills_list = document.getElementById('skills')

skill_bar.addEventListener('keypress', (e) => {
    if (e.key == 'Enter') {
        appendSkill(skill_bar)
    }
})

let appendSkill = (skill_bar) => {
    let new_skill = document.createElement("li");
    new_skill.setAttribute("id", skill_bar.value);
    new_skill.setAttribute("class", 'skill');
    new_skill.innerHTML = `${skill_bar.value} &#215;`
    skills_list.appendChild(new_skill)
    skill_bar.value = ''
}




skills_list.addEventListener('click', (e) => {
    let skill = e.target
    if (skill.className == 'skill') {
        skill.remove()
    }
})