<script setup lang="ts">

</script>

<template>
  <div id="update-notification" class="bg-white rounded-3xl">

    <!-- IF A UPDATE IS AVADIBLE -->
    <div class="py-14 px-8 space-y-4 h-full">
      <div class="bg-[#E5E7FA] py-1 px-4 inline-block rounded-full font-extrabold text-[#9DA2CB] select-none">v1.2</div>
      <div>
        <p class="text-white text-4xl font-medium">New Update is <br/>avadible!</p>
      </div>
      <div class="h-2/3 flex items-end py-6">
        <button class="w-full py-3 text-xl font-semibold rounded-xl text-[#9DA2CB] transition-all ease-in-out delay-100 hover:bg-[#d8daf0] bg-[#d1d3eb]">Update now</button>
      </div>
    </div>

  </div>
</template>

<style scoped>

</style>