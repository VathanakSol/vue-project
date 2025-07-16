<template>
  <!-- Navigation Bar -->
  <header>
    <div>
      <nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/about">About</RouterLink>
        <RouterLink to="/contact">Contact</RouterLink>
      </nav>
    </div>
  </header>

  <RouterView />
</template>

<style>
body {
  width: 100%;
  height: 100%;
  background-color: black;
  display: flex;
  color: white;
}
nav {
  height: 50px;
  background-color: greenyellow;
  width: 100vw;
  display: flex;
  text-decoration: none;
  justify-content: center;
  align-items: center;
  gap: 2rem;
}
</style>
