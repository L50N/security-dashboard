<script setup lang="ts">

</script>

<template>
  <div class="bg-white rounded-3xl mr-6 h-[38rem] py-12 px-8 -z-20">
    <div>
      <p class="text-lg text-gray-400">Stats</p>
      <p class="text-3xl font-medium">Percentage</p>
    </div>
    <div class="py-12 px-4 select-none flex justify-center">
      <!-- PERCENTAGE 01 -->
      <div class="h-52 w-52 rounded-[2.5rem] mr-[6rem] text-white bg-[#95A4FC69] flex items-center justify-center flex-col z-50">
        <p class="text-6xl font-semibold">55%</p>
        <p class="text-2xl font-medium">Docker</p>
      </div>

      <!-- PERCENTAGE 2 -->
      <div class="absolute h-36 w-36 rounded-[2.3rem] rotate-45 top-[452px] mr-[10rem] text-white bg-[#E7D4EEAD] flex items-center -z-10 justify-center flex-col">
        <div class="-rotate-45 flex flex-col text-center">
          <p class="text-4xl font-semibold">25%</p>
          <p class="text-lg font-medium">Reverse Pr...</p>
        </div>
      </div>

      <!-- PERCENTAGE 3 -->
      <div class="absolute h-32 w-32 rounded-full rotate-45 top-[402px] ml-[12rem] text-white bg-[#9DB5B247] flex items-center -z-10 justify-center flex-col">
        <div class="-rotate-45 flex flex-col text-center">
          <p class="text-3xl font-semibold">20%</p>
          <p class="text-base font-medium">Game Se...</p>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>

</style>