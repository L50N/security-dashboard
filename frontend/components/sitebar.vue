<template>
  <div class="h-screen fixed py-5 px-7 border-r-[1px] border-gray-200 bg-gray-50 inline-block min-w-[300px] select-none">
    <a href="/" class="hover:opacity-80 transition-all ease-in-out delay-100"><img src="/logo-dark.png" class="h-10"></a>

    <div class="flex flex-col justify-between h-full">
      <div class="py-12 space-y-1 cursor-pointer">

        <div class="cursor-pointer">
          <a class="flex flex-row space-x-2 items-center text-primary bg-[#f5f4f4] py-2 px-2 rounded-lg" href="">
            <div class="text-primary">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                stroke="currentColor" class="w-6 h-6">
                <path stroke-linecap="round" stroke-linejoin="round"
                  d="m2.25 12 8.954-8.955c.44-.439 1.152-.439 1.591 0L21.75 12M4.5 9.75v10.125c0 .621.504 1.125 1.125 1.125H9.75v-4.875c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21h4.125c.621 0 1.125-.504 1.125-1.125V9.75M8.25 21h8.25" />
              </svg>

            </div>
            <p class="cursor-pointer font-medium text-[15px]">Dashboard</p>
          </a>
        </div>

        <div class="cursor-pointer">
          <a class="flex flex-row space-x-2 items-center text-gray-700 hover:bg-[#f1f1f1] py-2 px-2 rounded-lg" href="">
            <div class="text-gray-400">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                stroke="currentColor" class="w-6 h-6">
                <path stroke-linecap="round" stroke-linejoin="round"
                  d="M15.362 5.214A8.252 8.252 0 0 1 12 21 8.25 8.25 0 0 1 6.038 7.047 8.287 8.287 0 0 0 9 9.601a8.983 8.983 0 0 1 3.361-6.867 8.21 8.21 0 0 0 3 2.48Z" />
                <path stroke-linecap="round" stroke-linejoin="round"
                  d="M12 18a3.75 3.75 0 0 0 .495-7.468 5.99 5.99 0 0 0-1.925 3.547 5.975 5.975 0 0 1-2.133-1.001A3.75 3.75 0 0 0 12 18Z" />
              </svg>
            </div>
            <p class="cursor-pointer font-medium text-[15px]">Firewall</p>
          </a>
        </div>

        <div class="cursor-pointer">
          <a class="flex flex-row space-x-2 items-center text-gray-700 hover:bg-[#f1f1f1] py-2 px-2 rounded-lg" href="">
            <div class="text-gray-400">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                stroke="currentColor" class="w-6 h-6">
                <path stroke-linecap="round" stroke-linejoin="round"
                  d="M5.25 14.25h13.5m-13.5 0a3 3 0 0 1-3-3m3 3a3 3 0 1 0 0 6h13.5a3 3 0 1 0 0-6m-16.5-3a3 3 0 0 1 3-3h13.5a3 3 0 0 1 3 3m-19.5 0a4.5 4.5 0 0 1 .9-2.7L5.737 5.1a3.375 3.375 0 0 1 2.7-1.35h7.126c1.062 0 2.062.5 2.7 1.35l2.587 3.45a4.5 4.5 0 0 1 .9 2.7m0 0a3 3 0 0 1-3 3m0 3h.008v.008h-.008v-.008Zm0-6h.008v.008h-.008v-.008Zm-3 6h.008v.008h-.008v-.008Zm0-6h.008v.008h-.008v-.008Z" />
              </svg>
            </div>
            <p class="cursor-pointer font-medium text-[15px]">Wireguard profiles</p>
          </a>
        </div>

        <div class="cursor-pointer">
          <a class="flex flex-row space-x-2 items-center text-gray-700 hover:bg-[#f1f1f1] py-2 px-2 rounded-lg" href="">
            <div class="text-gray-400">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                stroke="currentColor" class="w-6 h-6">
                <path stroke-linecap="round" stroke-linejoin="round"
                  d="M16.5 10.5V6.75a4.5 4.5 0 1 0-9 0v3.75m-.75 11.25h10.5a2.25 2.25 0 0 0 2.25-2.25v-6.75a2.25 2.25 0 0 0-2.25-2.25H6.75a2.25 2.25 0 0 0-2.25 2.25v6.75a2.25 2.25 0 0 0 2.25 2.25Z" />
              </svg>
            </div>
            <p class="cursor-pointer font-medium text-[15px]">Bruteforce</p>
          </a>
        </div>
      </div>

      <div class="mb-10">
        <div class="cursor-pointer">
          <a class="flex flex-row space-x-2 items-center text-gray-700 hover:bg-[#f1f1f1] py-2 px-2 rounded-lg" href="">
            <div class="text-gray-400">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                stroke="currentColor" class="w-6 h-6">
                <path stroke-linecap="round" stroke-linejoin="round"
                  d="M8.25 9V5.25A2.25 2.25 0 0 1 10.5 3h6a2.25 2.25 0 0 1 2.25 2.25v13.5A2.25 2.25 0 0 1 16.5 21h-6a2.25 2.25 0 0 1-2.25-2.25V15m-3 0-3-3m0 0 3-3m-3 3H15" />
              </svg>
            </div>
            <p class="cursor-pointer font-medium text-[15px]">Logout</p>
          </a>
        </div>
      </div>

    </div>
  </div>
</template>
