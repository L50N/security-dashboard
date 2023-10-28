<script setup lang="ts">

</script>

<template>
  <div class="min-h-screen flex items-center justify-center bg-gray-100 flex-col space-y-6">
    <div class="max-w-md w-full pb-12 px-8 sm:px-10 pt-16 bg-white rounded-3xl">
      <form @submit.prevent="login">
        <div class="mb-6 relative">
          <label for="email" class="block text-sm font-medium text-gray-600">E-Mail-Adresse</label>
          <div class="mt-1 relative rounded-[0.6rem] border focus-within:border-[#BDC0D8] px-1">
            <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="disabled"
                class="w-5 h-5 fill-gray-300">
                <path stroke-linecap="round" stroke-linejoin="round"
                  d="M15.75 6a3.75 3.75 0 11-7.5 0 3.75 3.75 0 017.5 0zM4.501 20.118a7.5 7.5 0 0114.998 0A17.933 17.933 0 0112 21.75c-2.676 0-5.216-.584-7.499-1.632z" />
              </svg>

            </div>
            <input v-model="email" type="email" id="email"
              class="block w-full py-2 pl-10 pr-4 border-transparent rounded-[0.6rem] focus:outline-none focus:border-[#BDC0D8] focus:ring-0 text-[0.9rem] flex items-center"
              placeholder="Deine E-Mail-Adresse" />
          </div>
        </div>
        <div class="mb-4 relative">
          <label for="password" class="block text-sm font-medium text-gray-600">Passwort</label>
          <div
            class="mt-1 relative rounded-[0.6rem] border focus-within:border-[#BDC0D8] focus-within:ring-2 focus-within:ring-[BDC0D8] px-1">
            <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="disabled"
                class="w-5 h-5 fill-gray-300">
                <path stroke-linecap="round" stroke-linejoin="round"
                  d="M15.75 5.25a3 3 0 013 3m3 0a6 6 0 01-7.029 5.912c-.563-.097-1.159.026-1.563.43L10.5 17.25H8.25v2.25H6v2.25H2.25v-2.818c0-.597.237-1.17.659-1.591l6.499-6.499c.404-.404.527-1 .43-1.563A6 6 0 1121.75 8.25z" />
              </svg>
            </div>
            <input v-model="password" type="password" id="password"
              class="block text-[0.9rem] w-full py-2 pl-10 pr-4 border-transparent rounded-[0.6rem] focus:outline-none focus:border-[#BDC0D8] focus:ring-0 flex items-center"
              placeholder="Dein Passwort" />
          </div>
        </div>
        <div class="mt-3">
          <button type="submit"
            class="w-full py-2 bg-[#BDC0D8] text-white rounded-xl text-lg font-semibold tracking-tight">Anmelden</button>
        </div>
      </form>
      <div class="flex justify-center py-3 select-none">
        <a href="https://example.com/" target="_blank" class="text-sm text-gray-400">Forgot password?</a>
      </div>
    </div>
    <div class="flex justify-center text-sm text-gray-400">
      <p>© Firewall Dashboard 2023</p>
    </div>
  </div>
</template>

<style scoped></style>