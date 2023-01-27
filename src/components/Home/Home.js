import { Link, Outlet } from 'react-router-dom';

import Header from '../Header/Header';

const Home = () => {
	return (
		<>
			<Header />
			<main>
				<Outlet />
			</main>
		</>
	);
};
export default Home;
