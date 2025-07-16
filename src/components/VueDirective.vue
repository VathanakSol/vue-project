<template>
  <main style="display: flex; justify-content: center; flex-direction: column">
    <p>Vue Directives</p>

    <form action="">
      <label for="">Username</label>
      <input type="text" v-model="name" placeholder="Enter your username" /><br />
      <label for="">Password</label>
      <input type="password" v-model="password" placeholder="Enter your password" />
    </form>
    <div>
      <p>{{ name }}</p>
      <!-- Do not display the password for security reasons -->
      <p v-if="password">Password is entered</p>
    </div>
  </main>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const name = ref('')
const password = ref('')
</script>
