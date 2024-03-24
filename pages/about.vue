<template>
    <section class="flex-grow container mx-auto p-4 text-center">
        <h1 class="text-7xl font-semibold mb-4">About</h1>

        <div class="divider"></div>

        <p class="py-6">
            Welcome to Habito, your personal companion on the journey to building better habits and leading a
            more productive life.
        </p>

        <h2 class="text-4xl font-bold">Why Choose Habito?</h2>

        <ul class="py-2">
            <li>
                Simple and Intuitive Design: Designed for ease of use.
            </li>
            <li>
                Customizable Tracking: Tailor the app to fit your lifestyle.
            </li>
            <li>
                Built-in Motivation: Includes features to keep you inspired and on track.
            </li>
            <li>
                Privacy and Security: Your data is encrypted and stored securely.
            </li>
        </ul>

        <p class="py-6">
            Thank you for choosing Habito to help you on your journey towards personal growth and
            self-improvement. We're excited to be a part of your success story!
        </p>

        <NuxtLink class="btn btn-neutral my-2" :to="{ name: 'login' }">Take Me Home</NuxtLink>
    </section>
</template>