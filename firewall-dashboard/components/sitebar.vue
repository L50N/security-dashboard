<script setup lang="ts">

</script>

<template>
  <div class="h-[100vh] justify-items-start rounded-r-2xl bg-white inline-block absolute w-64 py-48">

    <!-- MANAGEMENT CATEGORY -->
    <div class="px-6">
      <p class="px-3 text-gray-400 text-lg py-2">Management</p>
      <div class="select-none py-2">
        <div class="py-[0.35rem] bg-gray-100 rounded-[0.65rem] font-light text-xl cursor-pointer flex items-center">
          <div class="bg-black h-6 w-[0.4rem] rounded-full"></div>
          <div class="px-4 flex flex-row items-center">
            <div class="px-2">
              <img src="../public/Home.svg" class="w-[20px] h-[20px]">
            </div>
            <p>Home</p>
          </div>
        </div>
      </div>

      <div class="select-none">
        <div class="py-[0.35rem] rounded-[0.65rem] font-light text-xl cursor-pointer flex items-center"> <!-- NOT ACTIVE -->
          <div class="h-6 w-[0.4rem] rounded-full"></div> <!-- NOT ACTIVE -->
          <div class="px-4 flex flex-row items-center">
            <div class="px-2">
              <img src="../public/Groups.svg" class="w-[20px] h-[20px]">
            </div>
            <p>Groups</p>
          </div>
        </div>
      </div>
    </div>

    <!-- ADMINISTRATION CATEGORY -->
    <div class="px-6 py-16">
      <p class="px-3 text-gray-400 text-lg py-2">Administration</p>
      <div class="select-none">
        <div class="py-[0.35rem] rounded-[0.65rem] font-light text-xl cursor-pointer flex items-center"> <!-- NOT ACTIVE -->
          <div class="h-6 w-[0.4rem] rounded-full"></div> <!-- NOT ACTIVE -->
          <div class="px-4 flex flex-row items-center">
            <div class="px-2">
              <img src="../public/Profile.svg" class="w-[20px] h-[20px]">
            </div>
            <p>Profile</p>
          </div>
        </div>
      </div>

      <div class="select-none">
        <div class="py-[0.35rem] rounded-[0.65rem] font-light text-xl cursor-pointer flex items-center"> <!-- NOT ACTIVE -->
          <div class="h-6 w-[0.4rem] rounded-full"></div> <!-- NOT ACTIVE -->
          <div class="px-4 flex flex-row items-center">
            <div class="px-2">
              <img src="../public/Management.svg" class="w-[20px] h-[20px]">
            </div>
            <p>Management</p>
          </div>
        </div>
      </div>
    </div>

    <!-- FIREWALL DASHBOARD CREDITS --> <!-- TEMPORAERY DISABLED DUE BUGS! -->
    <div class="text-center flex justify-center items-end hidden">
      <p class="font-light text-gray-400">© Firewall Dashboard</p>
    </div>
  </div>
</template>

<style scoped>

</style>