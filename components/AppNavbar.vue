<script lang="ts" setup></script>

<template>
  <nav class="navbar bg-base-200 text-base-content">
    <div class="navbar-start">
      <div class="dropdown">
        <label tabindex="0" class="btn btn-ghost btn-circle">
          <i class="fa-solid fa-bars"></i>
        </label>
        <ul tabindex="0" class="menu menu-sm dropdown-content mt-3 z-[1] p-2 shadow bg-base-100 rounded-box w-52">
          <li><a>Profile</a></li>
          <li><a>Statistics</a></li>
          <li><a>About</a></li>
        </ul>
      </div>
    </div>
    <div class="navbar-center">
      <a class="btn btn-ghost normal-case text-xl">Habito</a>
    </div>
    <div class="navbar-end">
      <div class="dropdown dropdown-end">
        <label tabindex="0" class="btn btn-ghost btn-circle">
          <i class="fa-solid fa-user"></i>
        </label>
        <ul tabindex="0" class="menu menu-sm dropdown-content mt-3 z-[1] p-2 shadow bg-base-100 rounded-box w-52">
          <li><a>Sign In</a></li>
          <li><a>Sign Out</a></li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<style scoped></style>
