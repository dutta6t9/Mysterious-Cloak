let button = document.querySelector(".btn-container");
let image_container = document.querySelector(".img-container");
let end_button = document.querySelector(".end-btn-container");

let IS_STARTED = false;

// initial styling
image_container.style.display = "none";
end_button.style.display = "none";

/**
 * function for handling button clicks
 * @param {MouseEvent} event Event parameter
 * @returns {undefined}
 */
let handleBtnClick = (event) => {
  if (IS_STARTED === false) {
    IS_STARTED = true;
    button.style.display = "none";
    image_container.style.display = "flex";
    end_button.style.display = "flex";
    return;
  }

  if (IS_STARTED) {
    IS_STARTED = false;
    button.style.display = "flex";
    image_container.style.display = "none";
    end_button.style.display = "none";
    return;
  }
};

button.addEventListener("click", handleBtnClick);
end_button.addEventListener("click", handleBtnClick);