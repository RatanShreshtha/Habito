<script lang="ts" setup></script>

<template>
  <section class="flex-grow container mx-auto p-4 text-center">
    <h1 class="text-7xl font-semibold mb-4">Welcome to Habito</h1>

    <div class="divider"></div>

    <p class="py-6">
      Habito is a simple portal to track your habits and todo.
    </p>

    <NuxtLink class="btn btn-primary" :to="{ name: 'login' }">Get Started</NuxtLink>
  </section>
</template>

<style scoped></style>
