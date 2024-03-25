<template>
  <section class="flex-grow container mx-auto p-4 text-center">
    <h1 class="text-7xl font-semibold mb-4">Signing In ...</h1>

    <div class="divider"></div>

    <p class="py-6">
      Please wait while we log you in.
    </p>

    <span class="loading loading-bars loading-lg"></span>
  </section>
</template>

<script setup lang="ts">
const user = useSupabaseUser();
const { query } = useRoute();

watch(
  user,
  () => {
    if (user.value) {
      const to = (query.redirectTo as string) ?? '/';
      return navigateTo(to, {
        replace: true,
      });
    }
  },
  { immediate: true }
);
</script>