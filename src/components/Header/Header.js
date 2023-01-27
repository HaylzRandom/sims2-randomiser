import { Link } from 'react-router-dom';

import './header.css';

const Header = () => {
	return (
		<header>
			<h1>Sims 2 Randomiser</h1>
			<nav>
				<Link className='nav-link' to='generate-sim'>
					Generate a Sim
				</Link>
				<Link className='nav-link' to='generate-name'>
					Generate a Name
				</Link>
			</nav>
		</header>
	);
};
export default Header;
