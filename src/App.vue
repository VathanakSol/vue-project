<template>
  <!-- Navigation Bar -->
  <header>
    <div>
      <nav>
        <h1>Vue Project</h1>
        <RouterLink to="/" className="router-link">Home</RouterLink>
        <RouterLink to="/history" className="router-link">History</RouterLink>
        <RouterLink to="/about" className="router-link">About</RouterLink>
        <RouterLink to="/contact" className="router-link">Contact</RouterLink>
      </nav>
    </div>
  </header>

  <RouterView />
</template>

<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&family=Kantumruy+Pro:ital,wght@0,100..700;1,100..700&display=swap');
body {
  width: 100%;
  height: 100%;
  display: flex;
  color: black;
  font-family: 'Inter', sans-serif;
}

nav {
  height: 60px;
  background-color: greenyellow;
  width: 100vw;
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 2rem;
}

h1 {
  color: black;
  padding-right: 50vw;
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.router-link {
  text-decoration: none;
  font-weight: semibold;
  color: black;
}
</style>
