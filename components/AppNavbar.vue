<script lang="ts" setup>
const user = useSupabaseUser();
const supabase = useSupabaseClient();

const name = computed(
  () => user.value?.user_metadata.full_name
);
const profile = computed(
  () => user.value?.user_metadata.avatar_url
);

const logout = async () => {
  const { error } = await supabase.auth.signOut();

  if (error) {
    console.error(error);
    return;
  }

  await navigateTo('/');
};
</script>

<template>
  <nav class="navbar bg-base-200 text-base-content">
    <div class="navbar-start">
      <div class="dropdown" v-if="user">
        <label tabindex="0" class="btn btn-ghost btn-circle">
          <i class="fa-solid fa-bars"></i>
        </label>
        <ul tabindex="0" class="menu menu-sm dropdown-content mt-3 z-[1] p-2 shadow bg-base-100 rounded-box w-52">
          <li><a>Profile</a></li>
          <li><a>Statistics</a></li>
        </ul>
      </div>
    </div>
    <div class="navbar-center">
      <a class="btn btn-ghost normal-case text-3xl">Habito</a>
    </div>
    <div class="navbar-end">
      <div class="dropdown dropdown-end" v-if="user">
        <div tabindex="0" role="button" class="btn btn-ghost btn-circle avatar">
          <div class="w-10 rounded-full">
            <img :alt="name" :src="profile" />
          </div>
        </div>
        <ul tabindex="0" class="menu menu-sm dropdown-content mt-3 z-[1] p-2 shadow bg-base-100 rounded-box w-52">
          <li @click="logout"><a>Logout</a></li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<style scoped></style>
