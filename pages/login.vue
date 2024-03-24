<template>
    <section class="flex-grow container mx-auto p-4 text-center">
        <h1 class="text-7xl font-semibold mb-4">Sign In</h1>

        <div class="divider"></div>

        <p class="py-6">
            Use any of the following providers to SignIn.
        </p>

        <div class="flex justify-center">
            <div class="max-w-lg">
                <button class="btn btn-block font-bold my-2" @click="login('github')">
                    <img src="~/assets/logos/github.svg" class="size-4" /> Github
                </button>
                <button class="btn btn-block font-bold my-2" @click="login('google')">
                    <img src="~/assets/logos/google.svg" class="size-4" /> Google
                </button>
                <button class="btn btn-block font-bold my-2" @click="login('twitter')">
                    <img src="~/assets/logos/twitter.svg" class="size-4" /> Twitter
                </button>
            </div>
        </div>
    </section>
</template>

<script setup lang="ts">
const { query } = useRoute();
const supabase = useSupabaseClient();
const user = useSupabaseUser();

watchEffect(async () => {
    if (user.value) {
        await navigateTo(query.redirectTo as string, {
            replace: true,
        });
    }
});

const login = async (provider: any) => {
    const queryParams =
        query.redirectTo !== undefined
            ? `?redirectTo=${query.redirectTo}`
            : '';
    const redirectTo = `${useRuntimeConfig().public.baseUrl}/confirm${queryParams}`
    const { error } = await supabase.auth.signInWithOAuth({
        provider,
        options: { redirectTo },
    });

    if (error) {
        console.error(error);
    }
};
</script>