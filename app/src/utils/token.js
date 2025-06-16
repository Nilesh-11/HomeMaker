export const decodeJwtPayload = (token) => {
  if (!token) return null;

  try {
    const [, payload] = token.split(".");
    const base64 = payload.replace(/-/g, "+").replace(/_/g, "/");
    const decodedPayload = JSON.parse(atob(base64));

    const now = Math.floor(Date.now() / 1000);
    if (decodedPayload.exp && decodedPayload.exp < now) {
      console.warn("JWT token is expired");
      return null;
    }

    return decodedPayload;
  } catch (error) {
    console.error("Invalid JWT token", error);
    return null;
  }
};