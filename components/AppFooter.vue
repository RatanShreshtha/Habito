<template>
  <footer class="footer footer-center p-2 bg-base-200 text-base-content">
    <nav class="grid grid-flow-col gap-4">
      <NuxtLink class="link link-hover" :to="{ name: 'about' }">About</NuxtLink>
      <NuxtLink class="link link-hover" :to="{ name: 'contact' }">Contact</NuxtLink>
      <NuxtLink class="link link-hover" :to="{ name: 'license' }">License</NuxtLink>
    </nav>
    <nav>
      <div class="grid grid-flow-col gap-4">
        <NuxtLink to="https://facebook.com/RatanShreshtha" target="_blank">
          <i class="fa-brands fa-facebook fa-lg"></i>
        </NuxtLink>

        <NuxtLink to="https://www.linkedin.com/in/RatanShreshtha" target="_blank">
          <i class="fa-brands fa-linkedin fa-lg"></i>
        </NuxtLink>

        <NuxtLink to="https://twitter.com/RatanShreshtha" target="_blank">
          <i class="fa-brands fa-twitter fa-lg"></i>
        </NuxtLink>

        <NuxtLink to="https://github.com/RatanShreshtha" target="_blank">
          <i class="fa-brands fa-github fa-lg"></i>
        </NuxtLink>
      </div>
    </nav>
    <aside>
      <p>Copyright © 2024 - All right reserved</p>
    </aside>
  </footer>
</template>