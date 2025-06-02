<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Global Housing Price Estimator</title>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;600&display=swap" rel="stylesheet">
  <style>
    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      font-family: 'Poppins', sans-serif;
    }
    body {
      background: linear-gradient(to right, #c2e9fb, #a1c4fd);
      color: #333;
      line-height: 1.6;
    }
    header, footer {
      background-color: #003566;
      color: white;
      text-align: center;
      padding: 1rem;
    }
    nav a {
      margin: 0 1rem;
      color: white;
      text-decoration: none;
    }
    .container {
      max-width: 1000px;
      margin: 2rem auto;
      padding: 1rem;
      background-color: white;
      border-radius: 10px;
      box-shadow: 0 0 15px rgba(0, 0, 0, 0.2);
      text-align: center;
    }
    .house-image {
      max-width: 100%;
      border-radius: 10px;
      transition: transform 0.3s ease;
    }
    .house-image:hover {
      transform: scale(1.02);
    }
    .description {
      margin-top: 1rem;
      font-weight: 500;
    }
    .estimation-section input,
    .estimation-section select {
      padding: 0.6rem;
      margin-top: 1rem;
      width: 70%;
      border: 1.5px solid #0077b6;
      border-radius: 5px;
    }
    .estimation-section button {
      margin-top: 1rem;
      padding: 0.6rem 1.5rem;
      border: none;
      background-color: #00b4d8;
      color: white;
      font-weight: bold;
      border-radius: 5px;
      cursor: pointer;
      transition: background-color 0.3s;
    }
    .estimation-section button:hover {
      background-color: #0077b6;
    }
    .feedback {
      margin-top: 1rem;
      font-size: 1.1rem;
      font-weight: 600;
      color: #003566;
    }
    @media (max-width: 768px) {
      .estimation-section input,
      .estimation-section select {
        width: 90%;
      }
    }
    .intro {
      margin: 2rem auto;
      max-width: 900px;
      padding: 1rem;
      background-color: #f0f8ff;
      border-left: 5px solid #0077b6;
      border-radius: 8px;
    }
    .reset-btn {
      margin-top: 1rem;
      padding: 0.5rem 1.2rem;
      background-color: #ff6b6b;
      color: white;
      border: none;
      border-radius: 5px;
      font-weight: bold;
      cursor: pointer;
      transition: background-color 0.3s;
    }
    .reset-btn:hover {
      background-color: #d90429;
    }
  </style>
</head>
<body>
  <header>
    <h1>Global Housing Price Estimator</h1>
    <nav>
      <a href="#">Home</a>
      <a href="#">About the Project</a>
      <a href="#">Estimation Tool</a>
      <a href="#">Contact</a>
    </nav>
  </header>

  <section class="intro">
    <h2>About This Project</h2>
    <p>This web-based application is designed as an academic project to promote awareness of international real estate trends. Users can select details of residential properties from various countries and automatically receive an estimated price based on input factors, thereby gaining insight into global housing markets.</p>
  </section>

  <div class="container">
    <img class="house-image" id="houseImage" src="https://via.placeholder.com/800x400" alt="House">
    <div class="description" id="houseDesc">Modern detached home in Sydney, Australia.</div>

    <div class="estimation-section">
      <select id="location" onchange="displayHouse()">
        <option value="Sydney">Sydney</option>
        <option value="Paris">Paris</option>
        <option value="Tokyo">Tokyo</option>
        <option value="New York">New York</option>
        <option value="Mumbai">Mumbai</option>
        <option value="Cape Town">Cape Town</option>
        <option value="Toronto">Toronto</option>
        <option value="Berlin">Berlin</option>
      </select><br>
      <input type="text" id="city" placeholder="Enter City Name"><br>
      <input type="number" id="area" placeholder="Area in square feet"><br>
      <input type="number" id="bedrooms" placeholder="Number of bedrooms"><br>
      <input type="number" id="rooms" placeholder="Total rooms"><br>
      <button onclick="estimatePrice()">Show Estimated Price</button>
      <button class="reset-btn" onclick="resetForm()">Reset</button>
      <div class="feedback" id="feedback"></div>
    </div>
  </div>

  <footer>
    <p>&copy; 2025 Global Housing Estimator Project. Developed for academic purposes.</p>
  </footer>

  <script>
    const houseData = {
      "Sydney": { price: 950000, desc: 'Modern detached home in Sydney, Australia.', image: 'https://via.placeholder.com/800x400?text=Sydney+Home' },
      "Paris": { price: 1200000, desc: 'Apartment near Eiffel Tower in Paris, France.', image: 'https://via.placeholder.com/800x400?text=Paris+Flat' },
      "Tokyo": { price: 700000, desc: 'Compact home in central Tokyo, Japan.', image: 'https://via.placeholder.com/800x400?text=Tokyo+House' },
      "New York": { price: 1800000, desc: 'Luxury condo in Manhattan, New York.', image: 'https://via.placeholder.com/800x400?text=New+York+Condo' },
      "Mumbai": { price: 400000, desc: 'Urban flat in South Mumbai, India.', image: 'https://via.placeholder.com/800x400?text=Mumbai+Apartment' },
      "Cape Town": { price: 350000, desc: 'Beachside villa in Cape Town, South Africa.', image: 'https://via.placeholder.com/800x400?text=Cape+Town+Villa' },
      "Toronto": { price: 800000, desc: 'Suburban house in Toronto, Canada.', image: 'https://via.placeholder.com/800x400?text=Toronto+Home' },
      "Berlin": { price: 600000, desc: 'Modern apartment in Berlin, Germany.', image: 'https://via.placeholder.com/800x400?text=Berlin+Apartment' }
    };

    function displayHouse() {
      const loc = document.getElementById('location').value;
      const data = houseData[loc];
      document.getElementById('houseImage').src = data.image;
      document.getElementById('houseDesc').textContent = data.desc;
      document.getElementById('feedback').textContent = '';
    }

    function estimatePrice() {
      const location = document.getElementById('location').value;
      const city = document.getElementById('city').value.trim();
      const area = parseFloat(document.getElementById('area').value);
      const bedrooms = parseInt(document.getElementById('bedrooms').value);
      const rooms = parseInt(document.getElementById('rooms').value);

      const basePrice = houseData[location].price;
      let adjustedPrice = basePrice;

      if (!isNaN(area)) adjustedPrice += area * 30;
      if (!isNaN(bedrooms)) adjustedPrice += bedrooms * 20000;
      if (!isNaN(rooms)) adjustedPrice += rooms * 15000;

      const cityPart = city ? ` in ${city}` : '';
      const message = `🏡 The estimated price for the selected house configuration${cityPart} (${location}) is: $${adjustedPrice.toLocaleString()}`;
      document.getElementById('feedback').textContent = message;

      const estimation = {
        location,
        city,
        area,
        bedrooms,
        rooms,
        adjustedPrice,
        timestamp: new Date().toLocaleString()
      };
      localStorage.setItem('lastEstimation', JSON.stringify(estimation));
    }

    function resetForm() {
      document.getElementById('city').value = '';
      document.getElementById('area').value = '';
      document.getElementById('bedrooms').value = '';
      document.getElementById('rooms').value = '';
      document.getElementById('feedback').textContent = '';
      localStorage.removeItem('lastEstimation');
    }

    window.onload = function () {
      displayHouse();
      const last = localStorage.getItem('lastEstimation');
      if (last) {
        const data = JSON.parse(last);
        document.getElementById('location').value = data.location;
        document.getElementById('city').value = data.city;
        document.getElementById('area').value = data.area;
        document.getElementById('bedrooms').value = data.bedrooms;
        document.getElementById('rooms').value = data.rooms;
        displayHouse();
        estimatePrice();
      }
    };
  </script>
</body>
</html>
