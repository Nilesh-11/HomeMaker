import { lazy, Suspense, useMemo } from "react";
import { Routes, Route } from "react-router-dom";
import ProtectedRoute from "./ProtectedRoute";

const lazyImport = (path) => {
  const Component = lazy(() => import(`./../${path}`));
  return <Component />;
};

const publicRoutes = [
  { path: "/", component: "pages/Home" },
  { path: "/login", component: "pages/Login" },
  { path: "/signup", component: "pages/SignUp" },
  { path: "/dashboard", component: "pages/Dashboard" },
];

const protectedRoutes = [
  { 
    roles: ["user"],
    routes: [
      { path: "/user/dashboard", component: "pages/Dashboard" },
    ]
  },
  { 
    roles: ["admin"],
    routes: [
      { path: "/admin/dashboard", component: "pages/admin/Dashboard" },
    ]
  }
];

const AppRoutes = () => {
  const routeElements = useMemo(() => [
    ...publicRoutes.map(({ path, component }) => (
      <Route key={path} path={path} element={lazyImport(component)} />
    )),
    ...protectedRoutes.map(({ roles, routes }) => (
      <Route key={roles.join()} element={<ProtectedRoute allowedRoles={roles} />}>
        {routes.map(({ path, component }) => (
          <Route key={path} path={path} element={lazyImport(component)} />
        ))}
      </Route>
    )),
    <Route key="*" path="*" element={lazyImport("pages/NotFound")} />
  ], []);

  return (
    <Suspense fallback={<div>Loading...</div>}>
      <Routes>{routeElements}</Routes>
    </Suspense>
  );
};

export default AppRoutes;