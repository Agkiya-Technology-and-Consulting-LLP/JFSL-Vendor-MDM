<template>
  <aside :class="{ 'hidden': !isOpen, 'md:block': isOpen }"
    class="sidebar shadow-2xl text-white w-48 h-[calc(100vh-4rem)] py-4">
    <h2 class="text-xl font-bold mb-4">Sidebar</h2>

    <ul class="space-y-2 px-1">
      <router-link to="/welcome">
        <li class="d-flex justify-start items-center gap-2 pb-1">
          <i class="fa-solid fa-house h-6"></i>
          <a class="text-2xl mt-1">Onboarding</a>
        </li>
      </router-link>
      <router-link to="/companydetails">
        <li class="sidebar-link"><a class="text-lg">Company Details</a></li>
      </router-link>
      <router-link to="/Categorybusiness">
        <li class="sidebar-link"><a class="text-lg">Category Business</a></li>
      </router-link>
      <router-link to="/contactdetails">
        <li class="sidebar-link"><a class="text-lg">Contact Details</a></li>
      </router-link>
      <router-link to="/accountdetails">
        <li class="sidebar-link"><a class="text-lg">Account Details</a></li>
      </router-link>
      <router-link to="/documentdetails">
        <li class="sidebar-link"><a class="text-lg">Document</a></li>
      </router-link>
    </ul>


  </aside>

</template>

<script>
export default {
  props: {
    isOpen: {
      type: Boolean,
      required: true
    }
  }
};
</script>

<style scoped>
.sidebar {
  transition: transform 0.3s ease-in-out;
  transform: translateX(-100%);
}

.sidebar.md\:block {
  transform: translateX(0);
}

a {
  text-decoration: none;
}

.sidebar-link {
  padding-left: 2rem;
  margin-top: 0.5rem;
}

.sidebar-link a {
  color: #333;
}

.sidebar-link a:hover {
  color: #007bff;
}

.sidebar-link a {
  transition: color 0.3s ease-in-out;
}
</style>