import { NavLink } from "react-router-dom";
import { useSelector } from 'react-redux';

import "./ProductGrid.css";
import ProductGridItem from "./ProductGridItem/ProductGridItem";
// import { clearProductDetails } from "../../store/productDetails";

export default function ProductGrid() {
    const products = useSelector(state => Object.values(state.products));
    return (
        <div className="ProductGridWrapper">
            <div className="ProductGrid">
                {products.map((product, i) =>
                    <NavLink key={i} to={`/listing/${product.id}`} style={{ textDecoration: 'none' }}>
                        <ProductGridItem product={product} />
                    </NavLink>)
                }
            </div >
        </div>
    );
}
