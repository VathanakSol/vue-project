<template>
  <div>
    <h1>This is Reactivity Action</h1>
    <input type="text" v-model="user.name" placeholder="Enter your name" />
    <input type="number" v-model="user.age" placeholder="Enter your age" />
    <p v-on:click="increment">Count: {{ count }}</p>
    <p>Username: {{ user.name }}</p>
    <p>Age: {{ user.age }}</p>
  </div>
</template>

<style>
p {
  cursor: pointer;
  color: white;
}
</style>

<script setup lang="ts">
import { ref, reactive } from 'vue'

const count = ref(0)

const user = reactive({
  name: '',
  age: '',
})

const increment = () => {
  count.value++
}
</script>
