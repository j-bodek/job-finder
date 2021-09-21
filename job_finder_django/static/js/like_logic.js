let add_like_btns = document.querySelectorAll('.add_like')

add_like_btns.forEach(btn => {
    btn.addEventListener('click', (e) => {

        // get offer id
        let offer_id = btn.id.replace('click_', '')

        // create hidden form
        let form_id = 'form_' + offer_id
        let form = document.getElementById(form_id)

        // Check if heart is empty or already liked
        if (btn.childNodes[1].classList.contains('empty_heart')) {

            // append offer values to form
            let offer_data = document.querySelectorAll(offer_id)
            offer_data.forEach(data => {
                let value = data.textContent ? data.textContent : data.getAttribute('src')
                let name = data.dataset.name

                let input = document.createElement("input");

                input.setAttribute("type", "hidden");

                input.setAttribute("name", name);

                input.setAttribute("value", value);
                //append to form element
                form.appendChild(input);
            })

            // add offer id
            let input = document.createElement("input");

            input.setAttribute("type", "hidden");

            input.setAttribute("name", 'id');

            input.setAttribute("value", offer_id);
            //append to form element
            form.appendChild(input);

        } else {

            let input = document.createElement("input");

            input.setAttribute("type", "hidden");

            input.setAttribute("name", 'delete');

            input.setAttribute("value", offer_id);
            //append to form element
            form.appendChild(input);
        }


        // submit form
        form.submit();




    })
})