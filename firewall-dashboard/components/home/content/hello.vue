<script setup lang="ts">

</script>

<template>
  <div class="px-6">
    <div class="rounded-3xl space-y-1 py-12 px-8 bg-white">

      <!-- WELCOME TITLE -->
      <p class="text-lg text-gray-400">Dashboard Overview</p>
      <div class="flex items-center flex-row">
        <p class="text-3xl font-medium">Hello, Leon</p><img class="select-none px-3 h-10" src="../../../public/waving-hand_1f44b.png">
      </div>

      <!-- USER INFORMATION -->
      <div class="grid grid-cols-[190px,2fr] pt-8">
        <div class="text-lg text-gray-600 pt-1">
          <p class="select-none">October 30, 2023</p>
        </div>
        <div>
          <p class="text-3xl font-medium pb-3">
            New rule added!
          </p>
          <p class="text-gray-400">
            Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod
          </p>
        </div>
      </div>
      <div class="grid grid-cols-[190px,2fr] pt-8">
        <div class="text-lg text-gray-600 pt-1">
          <p class="select-none">October 23, 2023</p>
        </div>
        <div>
          <p class="text-3xl font-medium pb-3">
            User has been created!
          </p>
          <p class="text-gray-400">
            Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>

</style>