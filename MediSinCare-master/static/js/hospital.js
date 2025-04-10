// Select elements for patient reviews, cards, login form, and slider containers
const slides = document.querySelectorAll(".patientReview");
const cards = document.querySelectorAll(".card");
const closeBtn = document.getElementById("closeBtn");
const connectBtn = document.getElementById("connectBtn");
const emailInput = document.getElementById("email");
const passInput = document.getElementById("pass");
const sliderContainer = document.getElementById("sliderContainer");
const prevBtn = document.getElementById("prevBtn");
const nextBtn = document.getElementById("nextBtn");

const doctorSliderContainer = document.getElementById("doctorSliderContainer");
const specialitySliderContainer = document.getElementById("specialitySliderContainer");
const patientSliderContainer = document.getElementById("patientSliderContainer");

let currentIndex = 0; // Initialize current index for main slider
let doctorIndex = 0;
let specialityIndex = 0;
let patientIndex = 0; // Patient slider index

// Initialize main slider layout
function initializeSlider() {
    slides.forEach((slide, index) => {
        slide.style.left = `${index * 100}%`;
    });
    updateSlidePosition(); // Set the initial position for the main slider
}

// Update main slider position based on currentIndex
function updateSlidePosition() {
    sliderContainer.style.transform = `translateX(-${currentIndex * 100}%)`;
}

// Automatic slide transition every 3 seconds
setInterval(() => {
    moveSlide(1); // Automatically move to next slide every 3 seconds
}, 3000);

// Move main slider based on direction (1 for next, -1 for previous)
function moveSlide(direction) {
    const totalSlides = slides.length;
    currentIndex = (currentIndex + direction + totalSlides) % totalSlides; // Loop through slides
    updateSlidePosition(); // Update main slider position
}

// Manual navigation (next and previous) for main slider
prevBtn.addEventListener("click", () => moveSlide(-1));
nextBtn.addEventListener("click", () => moveSlide(1));

// Card click event to show modal with card details
cards.forEach((card) => {
    card.addEventListener("click", () => {
        const detailModal = document.querySelector(".detail");
        const contentElement = document.querySelector(".content");

        // Populate modal content with card data
        contentElement.innerHTML = `
            <img src="${card.querySelector("img").src}" alt="Card Image">
            <div class="contentText">
                <h1>${card.querySelector("h3").textContent}</h1>
                <p>${card.querySelector("p").textContent}</p>
            </div>
        `;

        // Show modal
        detailModal.style.display = "block";

        // Close modal on button click
        closeBtn.addEventListener("click", () => {
            detailModal.style.display = "none";
        });
    });
});

// Connect button click event to validate login
connectBtn.addEventListener("click", () => {
    const email = emailInput.value.trim();
    const pass = passInput.value.trim();

    if (!email || !pass) {
        alert("Please enter both email and password.");
    } else {
        alert("You are logged in!");
    }
});

// Initialize the main slider layout
initializeSlider();

// Doctor slider functionality
function moveDoctorSlide(direction) {
    const slides = document.querySelectorAll('#doctorSliderContainer .slide');
    doctorIndex = (doctorIndex + direction + slides.length) % slides.length;
    updateDoctorSlider();
}

// Speciality slider functionality
function moveSpecialitySlide(direction) {
    const slides = document.querySelectorAll('#specialitySliderContainer .slide');
    specialityIndex = (specialityIndex + direction + slides.length) % slides.length;
    updateSpecialitySlider();
}

// Update doctor slider display
function updateDoctorSlider() {
    const slides = document.querySelectorAll('#doctorSliderContainer .slide');
    slides.forEach((slide, index) => {
        slide.style.display = index === doctorIndex ? 'block' : 'none';
    });
}

// Update speciality slider display
function updateSpecialitySlider() {
    const slides = document.querySelectorAll('#specialitySliderContainer .slide');
    slides.forEach((slide, index) => {
        slide.style.display = index === specialityIndex ? 'block' : 'none';
    });
}

// Manual doctor slider navigation (previous and next buttons)
const prevDoctorBtn = document.getElementById("prevDoctorBtn");
const nextDoctorBtn = document.getElementById("nextDoctorBtn");
prevDoctorBtn.addEventListener("click", () => moveDoctorSlide(-1));
nextDoctorBtn.addEventListener("click", () => moveDoctorSlide(1));

// Manual speciality slider navigation (previous and next buttons)
const prevSpecialityBtn = document.getElementById("prevSpecialityBtn");
const nextSpecialityBtn = document.getElementById("nextSpecialityBtn");
prevSpecialityBtn.addEventListener("click", () => moveSpecialitySlide(-1));
nextSpecialityBtn.addEventListener("click", () => moveSpecialitySlide(1));

// Initialize the sliders on page load
updateDoctorSlider();
updateSpecialitySlider();

// Patient slider functionality
function movePatientSlide(direction) {
    const slides = document.querySelectorAll('#patientSliderContainer .slide');
    patientIndex = (patientIndex + direction + slides.length) % slides.length; // Loop through slides
    updatePatientSlider(); // Update the slider display
}

// Update patient slider display
function updatePatientSlider() {
    const slides = document.querySelectorAll('#patientSliderContainer .slide');
    slides.forEach((slide, index) => {
        slide.style.display = index === patientIndex ? 'block' : 'none'; // Show current slide
    });
}

// Initialize the patient slider on page load
updatePatientSlider();

// Add event listeners for previous and next buttons for patient slider
const prevPatientBtn = document.getElementById("prevPatientBtn");
const nextPatientBtn = document.getElementById("nextPatientBtn");
prevPatientBtn.addEventListener("click", () => movePatientSlide(-1)); // Move to the previous slide
nextPatientBtn.addEventListener("click", () => movePatientSlide(1)); // Move to the next slide
