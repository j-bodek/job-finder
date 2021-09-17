// // SEARCH

// const inputField = document.querySelector('.chosen-value');
// const dropdown = document.querySelector('.value-list');
// const dropdownArray = [...document.querySelectorAll('li')];

// let valueArray = [];
// dropdownArray.forEach(item => {
//     valueArray.push(item.textContent);
// });

// const closeDropdown = () => {
//     dropdown.classList.remove('open');
// }

// inputField.addEventListener('input', () => {
//     dropdown.classList.add('open');
//     let inputValue = inputField.value.toLowerCase();
//     let valueSubstring;
//     if (inputValue.length > 0) {
//         for (let j = 0; j < valueArray.length; j++) {
//             if (!(inputValue.substring(0, inputValue.length) === valueArray[j].substring(0, inputValue.length).toLowerCase())) {
//                 dropdownArray[j].classList.add('closed');
//             } else {
//                 dropdownArray[j].classList.remove('closed');
//             }
//         }
//     } else {
//         for (let i = 0; i < dropdownArray.length; i++) {
//             dropdownArray[i].classList.remove('closed');
//         }
//     }
// });

// dropdownArray.forEach(item => {
//     item.addEventListener('click', (evt) => {
//         inputField.value = item.textContent;
//         dropdownArray.forEach(dropdown => {
//             dropdown.classList.add('closed');
//         });
//     });
// })

// inputField.addEventListener('focus', () => {
//     inputField.placeholder = 'Type to filter';
//     dropdown.classList.add('open');
//     dropdownArray.forEach(dropdown => {
//         dropdown.classList.remove('closed');
//     });
// });

// inputField.addEventListener('blur', () => {
//     inputField.placeholder = 'Select state';
//     dropdown.classList.remove('open');
// });

// document.addEventListener('click', (evt) => {
//     const isDropdown = dropdown.contains(evt.target);
//     const isInput = inputField.contains(evt.target);
//     if (!isDropdown && !isInput) {
//         dropdown.classList.remove('open');
//     }
// });

// SEARCH

const inputField = document.querySelectorAll('.chosen-value');
const dropdowns = document.querySelectorAll('.value-list');
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

        let dropdownArray = label.querySelectorAll('li')
        let valueArray = returnValueArray(dropdownArray)

        dropdown.classList.add('open');
        let inputValue = input.value.toLowerCase();
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
        label = input.closest("label");
        dropdown = label.querySelector('.value-list')
        inputField.placeholder = 'Type to filter';
        dropdown.classList.add('open');
        dropdownArray = label.querySelectorAll('li')
        dropdownArray.forEach(dropdown => {
            dropdown.classList.remove('closed');
        });


    });
})




dropdowns.forEach(list => {
    list.addEventListener('click', (e) => {
        let input = list.closest("label").querySelector('.chosen-value');
        displayChoosenValue(e.target, input)
    })
})



let displayChoosenValue = (item, input) => {

    input.value = item.textContent;

}


// inputField.forEach(input => {
//     input.addEventListener('focus', () => {
//         input.placeholder = 'Type to filter';
//         dropdown.classList.add('open');
//         dropdownArray.forEach(dropdown => {
//             dropdown.classList.remove('closed');
//         });
//     });
// })

// inputField.forEach(input => {
//     input.addEventListener('blur', () => {
//         console.log('blur');
//         inputField.placeholder = 'Search Industry';
//         let label = input.closest("label");
//         let dropdown = label.querySelector('.value-list')
//         dropdown.classList.remove('open');
//     });
// })


document.addEventListener('click', (evt) => {
    if (evt.target.className !== 'chosen-value' && evt.target.className !== 'value-list') {
        dropdown.classList.remove('open');
    }
});




// SKILLS
let skill_bar = document.getElementById('skill_bar')
let skill_bar_level = document.getElementById('skill_bar_level')
let skills_list = document.getElementById('skills')

skill_bar_level.addEventListener('focus', () => {
    skill_bar_level.placeholder = 'From 1-5'
})

skill_bar.addEventListener('keypress', (e) => {
    if (e.key == 'Enter' && skill_bar.value && 0 < skill_bar_level.value && skill_bar_level.value <= 5) {
        appendSkill(skill_bar)
    }
})

skill_bar_level.addEventListener('keypress', (e) => {
    if (e.key == 'Enter' && skill_bar.value && 0 < skill_bar_level.value && skill_bar_level.value <= 5) {
        appendSkill(skill_bar)
    }
})

let appendSkill = (skill_bar) => {
    let new_skill = document.createElement("li");
    new_skill.setAttribute("id", skill_bar.value);
    new_skill.setAttribute("class", 'skill');
    new_skill.setAttribute('title', "Click to delete");
    new_skill.innerHTML = `Skill: ${skill_bar.value}  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; level: ${skill_bar_level.value}`

    let input = document.createElement("input");
    input.setAttribute('type', 'hidden');
    input.setAttribute('name', 'user_skills_list[]');
    input.setAttribute('value', `${skill_bar.value}--${skill_bar_level.value}`);
    new_skill.appendChild(input)

    skills_list.appendChild(new_skill)
    skill_bar.value = ''
    skill_bar_level.value = ''
}




skills_list.addEventListener('click', (e) => {
    let skill = e.target
    if (skill.className == 'skill') {
        skill.remove()
    }
})